from art_decode_dict import standard_num_decode_dic, standard_num_decode_dic_rev

def art_num_to_string_standard(txt):
 nums = standard_num_decode_dic
 num_keys = standard_num_decode_dic_rev
 lines = txt.splitlines()
 cursor_pos=0
 res=''
 # For art library standard font only checking 3rd line is enough
 while cursor_pos<len(lines[2]):
  # Since 4 has longest identifying string we check it first
  try:
   digit = nums[lines[2][cursor_pos:cursor_pos+len(num_keys['4'])]]
   cursor_pos+=len(num_keys['4'])
   res+=digit
  except:
   # if that doesn't match, we check for all other numbers except 1
   try:
    digit = nums[lines[2][cursor_pos:cursor_pos+len(num_keys['0'])]]
    cursor_pos+=len(num_keys['0'])
    res+=digit
   except:
    # if all of the above failed then it has to be either 1 OR there is some error thin the input itself
    try:
     digit = nums[lines[2][cursor_pos:cursor_pos+len(num_keys['1'])]]
     cursor_pos+=len(num_keys['1'])
     res+=digit
    except:
     raise KeyError

 return res
 