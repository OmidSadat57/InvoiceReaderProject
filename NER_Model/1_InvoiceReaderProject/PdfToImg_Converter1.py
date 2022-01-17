
from glob import glob
from pdf2image import convert_from_path

invoices_paths = glob('C:/Users/Admin/Desktop/all_invoices/Invoices_Xing/*.pdf')
target_folder_path = 'C:/Users/Admin/Desktop/all_invoices/Invoices_Xing_img/'

# We will only use limited number of invoices from each invoice type and therefore 
# we will generate IDs as bellow We should not forget to change the path 
# corresonding to our invoice type in  <invoices_paths> and <target_folder_path>
#
# We should also change the counter i corresondingly
# We only use 10-15 invoices from each type for our testing purpose
# 
# XING --> IDs from 0-249
# ProClipper --> IDs from 249-499
# Amazon --> IDs from 500-749

# XING: IDs from 0-249
#
# invoices_paths = glob('C:/Users/Admin/Desktop/all_invoices/Invoices_Xing/*.pdf')
# target_folder_path = 'C:/Users/Admin/Desktop/all_invoices/Invoices_Xing_img/'
i = 0
for path in invoices_paths:
    if i == 5:
        break
    pages = convert_from_path(path, 500)
    for page in pages:
        if i < 10:
            page.save(f'{target_folder_path}00{i}.png', "PNG")
        elif i >= 10 and i <= 99:
            page.save(f'{target_folder_path}0{i}.png', "PNG")
        else:
            page.save(f'{target_folder_path}{i}.png', "PNG")
    i += 1

# ProClipper: IDs from 250-499
#
# invoices_paths = glob('C:/Users/Admin/Desktop/all_invoices/Invoices_Pro-clipper/*.pdf')
# target_folder_path = 'C:/Users/Admin/Desktop/all_invoices/Invoices_Pro-clipper_img/'
# i = len(invoices_paths)
# for path in invoices_paths:
#     # if i == 255:
#     #     break
#     pages = convert_from_path(path, 500)
#     for page in pages:
#         page.save(f'{target_folder_path}{i}.png', "PNG")
#     i += 1

# Amazon: IDs from 500-749
#
# invoices_paths = glob('C:/Users/Admin/Desktop/all_invoices/Invoices_Amazon/*.pdf')
# target_folder_path = 'C:/Users/Admin/Desktop/all_invoices/Invoices_Amazon_img/'
# i = len(invoices_paths) + 250
# for path in invoices_paths:
#     # if i == 505:
#     #     break
#     pages = convert_from_path(path, 500)
#     for page in pages:
#         page.save(f'{target_folder_path}{i}.png', "PNG")
#     i += 1