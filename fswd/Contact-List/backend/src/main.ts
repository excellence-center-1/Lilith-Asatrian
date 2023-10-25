import { NestFactory } from '@nestjs/core';
import { ValidationPipe } from '@nestjs/common';
import { AppModule } from './app.module';
import { config } from 'dotenv';
import * as cookieParser from 'cookie-parser';

config();
async function bootstrap() {
  const PORT = process.env.HOST || 5001;
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(new ValidationPipe());
  const corsOptions = {
    origin: process.env.CLIENT_URL,
    credentials: true,
  };
  app.use(cookieParser());
  app.enableCors({
    // origin: '*',
    origin: `${process.env.CLIENT_URL}`,
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE,OPTIONS',
    credentials: true,
    exposedHeaders: ['Content-Range'],
  });
  await app.listen(PORT, ()=> {
    console.log(`Server is running on port ${PORT}`);
  })
}
bootstrap();
