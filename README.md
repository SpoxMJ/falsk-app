Matczak Michał spox098@gmail.com tel:731950803





For test tasks:
1. Test Dockerfile write command: 'docker build -t aplication .' and next step is 'docker run -d -p 4500:4500 application'
2. Test docker-compose write , docker-compose build , docker compose up, for test function application run on 5000 port,
3. For test method Post wait for get up database and  write'''curl -i -H "Content-Type: application/json" -X POST -d '{"msg":"your message"}' http://localhost:5000/echo''',
   For checkout added value to database write in website 'http://127.0.0.1:5000/list' for list all records in table
   and for malformed json curl -i -H "Content-Type: application/json" -X POST -d '{"msg":"your mesaage}' http://localhost:5000/echo
4. Test method GET go to website and write '127.0.0.1:5000/random' same with another GET '127.0.0.1:5000/list'
5. For check database initzialize with some data use 'docker exec -i e51aa5759fe6 mysql -hlocalhost -uroot -p' passoword is 'root'
and write command 'show databases;'i



