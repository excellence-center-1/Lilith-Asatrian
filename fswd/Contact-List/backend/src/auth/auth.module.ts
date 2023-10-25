import { Module } from '@nestjs/common';
import { PassportModule } from '@nestjs/passport';
import { AuthService } from './auth.service';
import { AuthController } from './auth.controller';
import { User } from 'database/models/users.model';
import { JwtModule } from '@nestjs/jwt'; 
import { JwtServiceModel } from './jwt.service';
import { SequelizeModule } from '@nestjs/sequelize';
@Module({
  imports: [
    PassportModule,
    SequelizeModule.forFeature([User]),
    JwtModule.register({
      secret: 'abcdef', 
      signOptions: { expiresIn: '7d' }, 
    }),
  ],
  providers: [AuthService, JwtServiceModel], 
  controllers: [AuthController],
})
export class AuthModule {}
