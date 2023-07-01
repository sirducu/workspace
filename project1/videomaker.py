




# def split_txt_into_multi_lines(input_str: str, line_length: int):
#     words = input_str.split(" ")
#     line_count = 0
#     split_input = ""
#     for word in words:
#         line_count += 1
#         line_count += len(word)
#         if line_count > line_length:
#             split_input += "\n"
#             line_count = len(word) + 1
#             split_input += split(word)
#             split_input += " "
#         else:
#             split_input += split(word)
#             split_input += " "
    
#     return split_input

from test import apireturn

news = apireturn()
print(news)