#### USER INPUT ####
def input_regx(inpt_str=None):
    """ Validates input identifier regex """
    pass

def clean_input_data(inpt_data=None):
    """  convert to upper ; split on delimiters ; etc. to prep data before using as a filter """
    pass


def filter_secid():
    """ Input prompt for """
    # print('All fields for a security must be entered on the same line')
    # print('Enter "q" to quit ')
    usr_inpt_secid = input('\nEnter Security Identifier:  ')
    return usr_inpt_secid

def filter_fields():
    """ Input prompt for fields """
    usr_inpt_flds = input("Enter Securitys Fields:  ")
    if usr_inpt_flds == 'q':
        return tuple(usr_inpt_flds)
    else:
        delimited_inpt_flds = re.split(r'[;:,\s|]+', usr_inpt_flds)
        return tuple(delimited_inpt_flds)
        # can add more text safeguards against bad input later 

def show_filter(filter_dictionary=None):
    # future safeguard
    # if filter_dictionary is None:
        # 
    print('\nFiltering File For Below:')
    for key,val in filter_dictionary.items():
        print(f"{key} : {val}")


def input_filters():
    """ Returns the secid and fields to searc/return"""
    print('\nEnter "q" to quit/exit loop...')
    filter_dict = collections.defaultdict(tuple)
    # runs until 'q' is entered
    while True:
        secid_filter_input = filter_secid()
        if secid_filter_input == 'q':
            break
        filter_field_input =  filter_fields()
        if filter_field_input == 'q':
            break
        filter_dict.update({secid_filter_input:filter_field_input})
    show_filter(filter_dict)
    return filter_dict
