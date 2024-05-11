from Data.encrypt import rot13
import os, csv, logging

def data():
    d = {}
    new = ['USERNAME', 'ACCOUNT TYPE', 'NAME', 'FATHER NAME', 'CNIC', 'PIN', 'BALANCE', 'LAST ACTIVE SESSION']

    filename = os.path.join('Data', 'userdata.csv')
    with open(filename, "a") as ap:
        if (os.path.getsize(filename)) <= 0:
            logging.info("creting a new file as '{}' in dir '{}'".format(filename, os.getcwd()))
            wr = csv.writer(ap)
            wr.writerow(new)
            ap.close()
            return d
        
        else:
            with open(filename, "r") as rd:
                r = csv.reader(rd)
                for indiv_user_info in r:
                    if (indiv_user_info == new) or (indiv_user_info == []):
                        continue
                    else:
                        try:
                            indiv_user_info[3] = rot13(indiv_user_info[3])
                            indiv_user_info[7] = float(indiv_user_info[7])
                            d[indiv_user_info[0]] = indiv_user_info[1],indiv_user_info[2],indiv_user_info[3],indiv_user_info[4],indiv_user_info[5],indiv_user_info[6],indiv_user_info[7],indiv_user_info[8],indiv_user_info[9]

                        except:
                            d[indiv_user_info[0]] = indiv_user_info[1],indiv_user_info[2],indiv_user_info[3],indiv_user_info[4],indiv_user_info[5],indiv_user_info[6],indiv_user_info[7],indiv_user_info[8],"None"

                return d