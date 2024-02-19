import express from 'express'
import dotenv from 'dotenv'
import { router } from './Router/router.js';
import path from 'path'

import cookieParser from 'cookie-parser'
dotenv.config();
const app = express();

app.use(cookieParser());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(path.resolve(), "public")));
app.set("view engine", "ejs");


app.use("/",router)

app.listen(1337,()=>{
    console.log("server running on:",1337);
})