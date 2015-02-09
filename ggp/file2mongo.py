__author__ = 'mengpeng'
import sys
from utils.mongo_juice import MongoJuice
from tweet import Tweet

if __name__ == '__main__':
    mongo = MongoJuice(coll_name=sys.argv[2])
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            if line.find('RT') == -1:
                tw = Tweet.fromstr(line)
                mongo.insert(tw.tomongo())
    print('{0} tweets are inserted into {1}.{2}'.format(mongo.count(), mongo.db_name, mongo.coll_name))