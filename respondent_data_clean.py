import argparse
parser= argparse.ArgumentParser()
parser.add_argument('contact_info_file')
parser.add_argument('other_info_file')
parser.add_argument('output_file')
args = parser.parse_args()


def respondent_data(contact_info_file,other_info_file,output_file):
    import pandas as pd
    import numpy as np
    
    contact = pd.read_csv(contact_info_file)
    other = pd.read_csv(other_info_file)

    merged = pd.merge(left=contact, right=other, left_on='respondent_id', right_on='respondent_id')
    merged['birthdate']=merged['birthdate'].astype(str)
    merged['birthdate']= merged['birthdate'].astype(str).str.pad(width=8, side='left', fillchar='0')
    merged['birthdate']= merged['birthdate'].apply(lambda x: x[4:]+"-"+x[:2]+"-"+x[2:4])
    #merged['address']= merged['address'].replace('\n',' ', regex= True)
    csv_file= merged.to_csv(output_file,index= False)
    return csv_file

if __name__ == '__main__':
    print(respondent_data(args.contact_info_file,args.other_info_file, args.output_file))