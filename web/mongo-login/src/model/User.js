import mongoose from 'mongoose'

const UserSchema = new mongoose.Schema({
    username:String,
    password:String
}) 

export const Users = mongoose.model("Users",UserSchema);
