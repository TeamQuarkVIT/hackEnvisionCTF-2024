import express from 'express'
import { homeRouterHandler } from '../controllers/slash.js';
import { loginHandler } from '../controllers/login.js';

export const router = express.Router();

router.get("/",homeRouterHandler)
router.post("/api/login",loginHandler)