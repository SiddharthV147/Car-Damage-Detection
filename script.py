import os
import shutil
import pandas as pd

image_directory = 'C:\\Users\\vedant golegaonkar\\Downloads\\DAMAGES.v5-updated-car-damage-dataset.tensorflow-20240411T061959Z-001\\DAMAGES.v5-updated-car-damage-dataset.tensorflow\\valid'

annotations_file = 'C:\\Users\\vedant golegaonkar\\Downloads\\DAMAGES.v5-updated-car-damage-dataset.tensorflow-20240411T061959Z-001\\DAMAGES.v5-updated-car-damage-dataset.tensorflow\\valid\\_annotations.csv'

crack_and_hole = os.path.join(image_directory, 'crack_and_hole')
medium_deformation = os.path.join(image_directory, 'medium_deformation')
severe_deformation = os.path.join(image_directory, 'severe_deformation')
severe_scratch = os.path.join(image_directory, 'severe_scratch')
windshield_damage = os.path.join(image_directory, 'windshield_damage')
slight_deformation = os.path.join(image_directory, 'slight_deformation')
slight_scratch = os.path.join(image_directory, 'slight_scratch')

os.makedirs(crack_and_hole, exist_ok=True)
os.makedirs(medium_deformation, exist_ok=True)
os.makedirs(severe_deformation, exist_ok=True)
os.makedirs(severe_scratch, exist_ok=True)
os.makedirs(windshield_damage, exist_ok=True)
os.makedirs(slight_deformation, exist_ok=True)
os.makedirs(slight_scratch, exist_ok=True)


annotations_df = pd.read_csv(annotations_file)

# Loop through annotations and move images to corresponding directories
for index, row in annotations_df.iterrows():
    image_filename = row['filename']  # assuming 'image_filename' is the column name containing image filenames
    annotation = row['class']  # assuming 'annotation' is the column name containing annotations

    # Check annotation and move the image accordingly
    if annotation == 'crack_and_hole':
        src = os.path.join(image_directory, image_filename)
        dst = os.path.join(crack_and_hole, image_filename)
        shutil.copy(src, dst)
    elif annotation == 'medium_deformation':
        src = os.path.join(image_directory, image_filename)
        dst = os.path.join(medium_deformation, image_filename)
        shutil.copy(src, dst)
    elif annotation == 'severe_deformation':
        src = os.path.join(image_directory, image_filename)
        dst = os.path.join(severe_deformation, image_filename)
        shutil.copy(src, dst)
    elif annotation == 'severe_scratch':
        src = os.path.join(image_directory, image_filename)
        dst = os.path.join(severe_scratch, image_filename)
        shutil.copy(src, dst)
    elif annotation == 'windshield_damage':
        src = os.path.join(image_directory, image_filename)
        dst = os.path.join(windshield_damage, image_filename)
        shutil.copy(src, dst)
    elif annotation == 'slight_deformation':
        src = os.path.join(image_directory, image_filename)
        dst = os.path.join(slight_deformation, image_filename)
        shutil.copy(src, dst)
    elif annotation == 'slight_scratch':
        src = os.path.join(image_directory, image_filename)
        dst = os.path.join(slight_scratch, image_filename)
        shutil.copy(src, dst)
    else:
        print(f"Unknown annotation found for {image_filename}: {annotation}")

print("Image segregation complete.")
