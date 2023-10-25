
import { Column, Model, Table, DataType, HasMany } from 'sequelize-typescript';
import { UserContact } from './users_contacts.model';

@Table({ tableName: 'contacts', timestamps: false  })
export class Contact extends Model<Contact> {
  @Column({ primaryKey: true, autoIncrement: true, allowNull: false })
  id: number;

  @Column({ allowNull: false })
  name: string;

  @Column({ allowNull: false})
  surname: string;

  @Column({allowNull: false})
  phone_number: string

  @Column({allowNull:true})
  work_place: Date

  @HasMany(() => UserContact)
  users_contacts: UserContact[];
}