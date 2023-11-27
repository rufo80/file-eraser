# file-eraser
extension_to_delete = "txt" 

days_threshold = 30  

folder_path_to_search = "/path/folder"

file_remover = FileEraser(extension_to_delete, days_threshold)

file_remover.remove_files(folder_path_to_search)
