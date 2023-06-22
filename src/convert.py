# Path to the original dataset

import csv
import os
from collections import defaultdict

import gdown
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from tqdm import tqdm

import src.settings as s


def download_dataset():
    archive_path = os.path.join(sly.app.get_data_dir(), "archive.zip")

    if not os.path.exists(archive_path):
        if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
            gdown.download(s.DOWNLOAD_ORIGINAL_URL, archive_path, quiet=False)
        if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
            for name, url in s.DOWNLOAD_ORIGINAL_URL:
                gdown.download(url, os.path.join(archive_path, name), quiet=False)
    else:
        sly.logger.info(f"Path '{archive_path}' already exists.")
    return unpack_if_archive(archive_path)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    def _create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]
        image_name = sly.fs.get_file_name_with_ext(image_path)
        curr_bboxes_class_data = image_name_to_data.get(image_name, [])
        for data in curr_bboxes_class_data:
            obj_class = data[1]
            bbox = list(map(int, data[0]))
            rect = sly.Rectangle(top=bbox[1], left=bbox[0], bottom=bbox[3], right=bbox[2])
            curr_label = sly.Label(rect, obj_class)
            labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    dataset_path = "/Users/almaz/Downloads/wind-turbine-detector-master"
    images_dirname = "images"
    anns_dirname = "annotations"
    ds_names = ["train", "valid", "test"]
    batch_size = 30

    obj_class = sly.ObjClass("wind turbine", sly.Rectangle)
    class_name_to_obj_class = {"wind turbine": obj_class}

    project = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta(obj_classes=[obj_class])

    images_folder = os.path.join(dataset_path, images_dirname)
    anns_folder = os.path.join(dataset_path, anns_dirname)

    for ds_name in ds_names:
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)
        if os.path.exists(os.path.join(anns_folder, f"{ds_name}_labels.csv")):
            with open(os.path.join(anns_folder, f"{ds_name}_labels.csv")) as f:
                csvreader = csv.reader(f, delimiter=",")
                image_name_to_data = defaultdict(list)
                for idx, row in enumerate(csvreader):
                    if idx == 0:
                        continue
                    if row[3] not in list(class_name_to_obj_class.keys()):
                        new_obj_class = sly.ObjClass(row[3], sly.Rectangle)
                        class_name_to_obj_class[row[3]] = new_obj_class
                        meta = meta.add_obj_class(new_obj_class)

                    curr_image_path = os.path.join(images_folder, ds_name, row[0])
                    if sly.fs.file_exists(curr_image_path):
                        image_name_to_data[row[0]].append((row[4:], class_name_to_obj_class[row[3]]))

        api.project.update_meta(project.id, meta.to_json())
        images_names = os.listdir(os.path.join(images_folder, ds_name))
        progress = tqdm(desc=f"Create dataset {ds_name}", total=len(images_names))
        for img_names_batch in sly.batched(images_names, batch_size=batch_size):
            img_pathes_batch = [
                os.path.join(images_folder, ds_name, im_name) for im_name in img_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [_create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)
            progress.update(len(img_names_batch))

    return project
