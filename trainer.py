import pandas as pd
import csv

def main():
    train_bidder_data =  pd.read_csv('train.csv')
    print("Done Reading Train Data")
    bids = pd.read_csv('bids.csv')
    print("Done Reading Bids Data")
    test_data = pd.read_csv('test.csv')
    print("DOne Read Test Data")



if __name__ == '__main__':
    main()