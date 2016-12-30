import json
import redis
import pymongo

def main():
    r = redis.Redis(host='123.207.147.252',port=6379,db=0)
    client = pymongo.MongoClient(host='127.0.0.1', port=12345)
    while True:
        # process queue as FIFO, change `blpop` to `brpop` to process as LIFO
        source, data = r.blpop(["zhilian:items"])
        item = json.loads(data)

	database = item["workplace"]
	collection = item["jobcategory"]

	db = client[database]
	coll = db[collection]

        coll.insert(item)
	print('process')
if __name__ == '__main__':
    main()
