import { Column, Model, Table, DataType, HasMany } from 'sequelize-typescript';
import { UserContact } from './users_contacts.model';

@Table({ tableName: 'users', timestamps: false })
export class User extends Model<User> {
  @Column({ primaryKey: true, autoIncrement: true, allowNull: false })
  id: number;

  @Column({ allowNull: false })
  username: string;

  @Column({ unique: true, allowNull: false })
  email: string;

  @Column({ allowNull: false })
  password: string;

  @Column({ type: DataType.DATE, allowNull: false, defaultValue: DataType.NOW })
  createdAt: Date;

  @HasMany(() => UserContact)
  users_contacts: UserContact[];
}
