from art_decode import art_num_to_string_standard
import art

if __name__ == "__main__":
 txt=art.text2art("146")
 assert art_num_to_string_standard(txt) == "146"
 print(art_num_to_string_standard(txt))