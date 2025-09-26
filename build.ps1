docker build -t caliban0204/searchquery:latest ./frontend/searchQuery
docker build -t caliban0204/add-book:latest ./frontend/addBook
docker build -t caliban0204/data_saver:latest ./dataSaver

docker push caliban0204/data_saver:latest
docker push caliban0204/add-book:latest 
docker push caliban0204/searchquery:latest