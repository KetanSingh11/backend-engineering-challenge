## Solution (Backend)

### Tech Stack
- Python v3.7 or above
- pytest

#### Steps to setup  
1. Go to the directory `shopping_api`

2. Install pip dependencies
    ```shell script
    pip install -r requirements.txt
    ```
   
3. Run the app (on port `5010` by default). 
    Type:   
    ```shell script
    export FLASK_APP=paradata_app
    flask run --port 5010
   ```
    
4. Go to any web-browser and type:
    ```shell script
    http://localhost:5010/test
    ```
    You should see "Hello, World!"


#### Backend Rest APIs  
Use any rest api client or `curl` command:  

- API `/list`:- Lists all the inventory present.
    ```shell script
    curl -X GET http://localhost:5010/list
    ```
    You should see the inventory you have.   

- API `/stock`:- Adds an item to the inventory
    ```shell script
    curl -X POST -H "Content-Type: application/json" -d '{"category": "Sporting Goods", "price": "$49.99", "name": "Football"}' "http://localhost:5010/stock"
    ```

- API `/buy`:- Buy an item from the inventory
    ```shell script
    curl -X POST -H "Content-Type: application/json" -d '{"category": "Sporting Goods", "name": "Football"}' "http://localhost:5010/buy"
    ```

    ```shell script
    curl -X POST -H "Content-Type: application/json" -d '{"category": "Sporting Goods", "name": "Bat"}' "http://localhost:5010/buy"
    ```


### Runing Test cases
- Run pytest:
    ```shell script
    pytest -v
    ```
