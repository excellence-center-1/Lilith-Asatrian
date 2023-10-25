import { Module } from '@nestjs/common';
import { ContactsController } from './contact.controller';
import { ContactService } from './contact.service';
import { Contact } from 'database/models/contacts.model';
import { SequelizeModule } from '@nestjs/sequelize';
import { UserContact } from 'database/models/users_contacts.model';
import { User } from 'database/models/users.model';
@Module({
  imports: [SequelizeModule.forFeature([Contact, UserContact, User])],
  controllers: [ContactsController],
  providers: [ContactService],
})
export class ContactModule {}
