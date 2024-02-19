import mongoose from "mongoose";
import dotenv from 'dotenv'

dotenv.config();

export const connectDB = async () => {

    mongoose.set('strictQuery', false);
    const conn = await mongoose.connect(process.env.MONGO_URI, {
        dbName: "quark-ctf-web"
    }).then(() => console.log("database connected"))
    .catch((e) => { console.log(e) })
}
