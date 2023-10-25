import {
  BelongsTo,
  Column,
  ForeignKey,
  Model,
  Table,
} from 'sequelize-typescript';
import { User } from './users.model';
import { Contact } from './contacts.model';

@Table({ tableName: 'users_contacts', timestamps: false })
export class UserContact extends Model<UserContact> {
  @Column({ primaryKey: true, autoIncrement: true, allowNull: false })
  id: number;

  // @BelongsTo(() => User, 'id')
  @ForeignKey(() => User)
  @Column({ allowNull: false })
  user_id: number;

  // @BelongsTo(() => Contact, 'id')
  @ForeignKey(() => Contact)
  @Column({ allowNull: false })
  contact_id: number;
}