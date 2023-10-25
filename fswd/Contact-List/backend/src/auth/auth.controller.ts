import { Controller, Post, Body, Res, Put } from '@nestjs/common';
import { Response } from 'express';
import { AuthService } from './auth.service';
import { CreateUserDto } from './dto/create-user.dto';
import { User } from 'database/models/users.model';
import { LoginDto } from './dto/login-user.dto';
import { HttpException, HttpStatus } from '@nestjs/common';
@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @Post('register')
  async register(@Body() createUserDto: CreateUserDto): Promise<User> {
    const { username, email, password } = createUserDto;
    const user = await this.authService.register(username, email, password);
    return user;
  }

  @Put('login')
  async login(@Body() loginData: LoginDto) {
    console.log("TRY LOGIN");
    const { username, password } = loginData;
    console.log(username, password);
    const user = await this.authService.login(username, password);
   // console.log("user", user);
    if (user) {
      // Return the user ID in the response
      return { userId: user.id };
    } else {
      throw new HttpException('Invalid email or password', HttpStatus.UNAUTHORIZED);
    }
  }
  
}
