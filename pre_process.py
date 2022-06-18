import json
import csv
import glob
import pandas as pd

def set_data():
    f = open('data.csv', 'w')
    writer = csv.writer(f)

    header = ['conference','Date','title','id','IMPACT','SUBSTANCE','APPROPRIATENESS','MEANINGFUL_COMPARISON','SOUNDNESS_CORRECTNESS','ORIGINALITY','CLARITY','REVIEWER_CONFIDENCE','accepted','RECOMMENDATION','comments']
    writer.writerow(header)
    json_keys = ['IMPACT','SUBSTANCE','APPROPRIATENESS','MEANINGFUL_COMPARISON','SOUNDNESS_CORRECTNESS','ORIGINALITY','CLARITY','REVIEWER_CONFIDENCE','accepted','RECOMMENDATION','comments']

    conferences_dir = [x for x in glob.glob("data/*") if x not in glob.glob("data/*.txt")]
    c_r = conferences_dir
    for i in c_r:
        k = 0
        conference = i.split('/')[1]
        directories = [i+'/'+x for x in ['train','test','dev']]
        for d in directories:
            reviews_dir = d + '/reviews'
            reviews = glob.glob(reviews_dir+'/*.json')
            for r in reviews:
                json_review = json.load(open(r))
                try:
                    Date = json_review['DATE_OF_SUBMISSION']
                except:
                    Date = get_date(d,r.split('/')[-1].split('.')[0])
                title = json_review['title']
                if len(json_review['reviews']) == 0:
                    r_j_data = []
                    ID = json_review['id']
                    for key in json_keys:
                        try:
                            r_j_data.append(json_review[key])
                        except:
                            try:
                                r_j_data.append(json_review[key])
                            except:
                                r_j_data.append(None)
                    row = [conference, Date, title, ID] + r_j_data
                    writer.writerow(row)
                    k += 1
                else:
                    for r_j in json_review['reviews']:
                        r_j_data =[]
                        ID = json_review['id']
                        for key in json_keys:
                            try:
                                r_j_data.append(r_j[key])
                            except:
                                try:
                                    r_j_data.append(json_review[key])
                                except:
                                    r_j_data.append(None)

                        row = [conference,Date,title,ID] + r_j_data
                        writer.writerow(row)
                        k+=1

        print(i , k)


    f.close()

#def specific_check():


def get_date(d,review_name):
    jsonpdf_dir = d + '/parsed_pdfs/'+ review_name +'.pdf.json'
    json_pdf = json.load(open(jsonpdf_dir))
    return json_pdf['metadata']['year']


if __name__ == '__main__':
    set_data()