import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './auth/auth.module';
import { SequelizeModule } from '@nestjs/sequelize';
import { ConfigModule } from '@nestjs/config';
import { User } from 'database/models/users.model';
import { Contact } from 'database/models/contacts.model';
import { UserContact } from 'database/models/users_contacts.model';
import { ContactModule } from './contact/contact.module';
@Module({
  
  imports: [
    ConfigModule.forRoot({
      envFilePath: `.env`
    }),
    SequelizeModule.forRoot({
      dialect: 'postgres',
      host: process.env.PG_HOST,
      port: Number(process.env.PG_PORT),
      username: process.env.PG_USER,
      password: process.env.PG_PASSWORD,
      database: process.env.PG_DATABASE,
      models: [User, Contact, UserContact]
    }),
    AuthModule,
    ContactModule,],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
