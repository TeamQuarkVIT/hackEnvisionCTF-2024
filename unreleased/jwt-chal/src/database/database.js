import mysql from "mysql2/promise";
import dotenv from 'dotenv';
dotenv.config();

let dbconnection;

export async function connect() {
  dbconnection = await mysql.createConnection({
    host: process.env.HOST,
    port: "3306",
    database: process.env.DB_NAME,
    user: process.env.NAME,
    password: process.env.PASSWORD,
  });
}

export async function disconnect() {
  if (dbconnection) {
    await dbconnection.end();
  }
}

export async function query({ query, values = [] }) {
  try {
    if (!dbconnection) {
      await connect();
    }

    const [results] = await dbconnection.execute(query, values);
    return results;
  } catch (error) {
    throw new Error(error.message);
  }
}
