import express from 'express'
import { connectDB } from './database/db.js';
import { router } from './router/router.js';

import dotenv from 'dotenv';
dotenv.config();

const app = express();

app.use(express.urlencoded({extended:true}))
app.use(express.json())
app.use("/",router)

app.set("view engine","ejs")
connectDB().then(()=>{
    app.listen(process.env.PORT,()=>{
        console.log("app listening on port:",process.env.PORT);
    })
})
