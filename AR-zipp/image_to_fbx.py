import os
import requests
import time

from lib.preprocessing import PreProcessing
from lib.blend_to_fbx import BlendToFBX

preprocessing = PreProcessing()
converter = BlendToFBX()


class ImageToFBX():
    def __init__(self) -> None:
        pass

    def image_to_fbx(self, file_path):
        print('')
        # Preprocessing
        ouput_path = 'statics/Images/After_preprocessing'
        preprocessing.run(file_path, ouput_path)
        preprocessing_result = preprocessing.file_save_path('OCR')

        # Image to blend file
        url = 'http://127.0.0.1:8001/blueprint_to_3D'

        data = {'ImagePath': preprocessing_result}

        response = requests.post(url, json=data)
        print(f'Status Code: {response.status_code}  /  Response Content : {response.text}')

        # if response.status_code == 200:   
        #     time.sleep(0.5)
        #     # Blend to fbx converter
        #     blend_name = response.text.replace('"','')
        #     blend_path = f"statics/blend_file/{blend_name}"

        #     fbx_dir = 'statics/fbx_file'
        #     converter.blend_to_fbx(blend_path, fbx_dir)

        #     print('convert successfully!')
        # else:
        #     print(f'make bled error : {preprocessing_result}')



if __name__ == '__main__':
    ItoFBX = ImageToFBX()

    file_dir = 'statics\\Images\\Original'
    file_list = os.listdir(file_dir)

    file_path = str(file_dir+'\\'+'image_000.jpg')
    ItoFBX.image_to_fbx(file_path)

    # for file in file_list[55:]:
    #     file_path = str(file_dir+'\\'+file)
    #     ItoFBX.image_to_fbx(file_path)