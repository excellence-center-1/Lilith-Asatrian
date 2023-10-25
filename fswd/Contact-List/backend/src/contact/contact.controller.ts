import { Controller, Get, Query, ParseIntPipe } from '@nestjs/common';
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
  
}
