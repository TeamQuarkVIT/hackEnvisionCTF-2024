import express from 'express'
import { homeController } from '../controllers/home.js';
import { handleRegistration, registerPage } from '../controllers/registration.js';
import { handleLogin, loginPage } from '../controllers/login.js';
import { profilePage } from '../controllers/profile.js';
import { handleGetAuthCode } from '../controllers/getAuthCode.js';
import { getUserNameUpdationPage, handleUserNameUpdation } from '../controllers/usernameUpdate.js';

export const router = express.Router();

router.get("/",homeController)
router.get("/register",registerPage)
router.get("/login",loginPage)
router.get("/profile/:id",profilePage)
router.post("/register",handleRegistration)
router.post("/login",handleLogin)

router.get('/get-auth-code',handleGetAuthCode)
router.get('/update-username',getUserNameUpdationPage)
router.post('/update-username',handleUserNameUpdation)
