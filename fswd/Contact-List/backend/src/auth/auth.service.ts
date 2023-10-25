import { Injectable, HttpStatus, HttpException } from '@nestjs/common';
import { User } from 'database/models/users.model';
import { InjectModel } from '@nestjs/sequelize';
import * as bcrypt from 'bcrypt';

@Injectable()
export class AuthService {
  constructor(
    @InjectModel(User)
    private userModel: typeof User,
  ) {}

  async register(
    username: string,
    email: string,
    password: string,
  ): Promise<User> {
      const existingUser = await this.userModel.findOne({ where: { email } });
      if (existingUser) {
        throw new HttpException(
          'User with this email already exists',
          HttpStatus.CONFLICT,
        );
      }
      try {
        // const hashedPassword = await bcrypt.hash(password, 10);
        const user = await this.userModel.create({ username, email, password  });
        return user;
      } catch (error) {
        throw new HttpException('User registration failed', HttpStatus.BAD_REQUEST);
      }
  }

  async login(username: string, password: string) {
    const user = await this.userModel.findOne({ where: { username } });
    console.log("aaaa", user);
    if (user) {
      const isPasswordValid = await bcrypt.compare(password, user.password);
  
      if (isPasswordValid) {
        console.log("bbbb", user);
        return user;
      }
    }
  
    return null;
  }
  
}