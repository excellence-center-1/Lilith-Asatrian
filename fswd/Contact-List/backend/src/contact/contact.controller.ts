import { Controller, Get, Query, ParseIntPipe, Post, Body } from '@nestjs/common';
import { ContactService } from './contact.service';

@Controller('contacts')
export class ContactsController {
  constructor(private contactsService: ContactService) {}

  @Get()
  getContacts(@Query('userId', ParseIntPipe) userId: number) {
    console.log("Start:");
    const contacts = this.contactsService.getContactsForUser(userId);

    return contacts;
  }

  @Post('add')
  addContact(@Query('userId', ParseIntPipe) userId: number, @Body() newContact: any) {
    console.log("NewContact: ", newContact);
    const createdContact = this.contactsService.addNewContactForUser(userId, newContact);

    return createdContact;
  }

}
