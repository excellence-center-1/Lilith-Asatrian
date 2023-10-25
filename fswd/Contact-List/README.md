## PostgreSQL Database Setup
Follow these steps to set up your PostgreSQL database for Contact List
1. **Log in to your PostgreSQL server:**
    ```bash
    sudo su postgres
    psql
    ```
2. **Create a new user named `contact` with the password '123':**
    ```sql
    CREATE USER contact WITH PASSWORD '123';   
3. **Create a new database named `contact_list`:**
    ```sql
    CREATE DATABASE contact_list;
    ```
### Client installation
```bash
cd client/
npm install
npm start
```
### Server installation
```bash
cd server/
```
Execute the following command to run the migrations
```bash
npx sequelize db:migrate
```

4. **Grant all privileges on the `contact_list` database to the `contact` user:**

```sql
    GRANT ALL PRIVILEGES ON DATABASE contact_list TO contact;
```

5. **Connect to the `contact_list` database:**

```sql
    \c contact_list
```
```bash
npm install
npm start
```