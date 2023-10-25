import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/sequelize';
import { User } from 'database/models/users.model';
import { Contact } from 'database/models/contacts.model';
import { UserContact } from 'database/models/users_contacts.model';

@Injectable()
export class ContactService {
  constructor(
    @InjectModel(User) private userModel: typeof User,
    @InjectModel(Contact) private contactModel: typeof Contact,
    @InjectModel(UserContact) private userContactModel: typeof UserContact,
  ) {}

  async getContactsForUser(userId: number): Promise<Contact[]> {
    try {
      const user = await this.userModel.findByPk(userId);

      if (!user) {
        throw new Error('User not found');
      }

      const userContacts = await this.userContactModel.findAll({
        where: { user_id: userId },
      });

      const contactIds = userContacts.map((uc) => uc.contact_id);

      const contacts = await this.contactModel.findAll({
        where: { id: contactIds },
      });

      return contacts;
    } catch (error) {
      throw new Error('Failed to get contacts for the user: ' + error.message);
    }
  }
}
