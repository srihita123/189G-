from src_code.stage_3_code.Result_Loader import Result_Loader

if 1:
    result_obj = Result_Loader('saver', '')
    result_obj.result_destination_folder_path = '../../result/stage_3_result/CNN_ORL_'
    result_obj.result_destination_file_name = 'prediction_result'

    result_obj.load()
    print('Result:', result_obj.data)