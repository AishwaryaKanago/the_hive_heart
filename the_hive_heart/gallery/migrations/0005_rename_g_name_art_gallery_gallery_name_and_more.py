# Generated by Django 4.0.1 on 2022-01-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_rename_paintings_painting_remove_customer_c_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='art_gallery',
            old_name='G_name',
            new_name='Gallery_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='C_address',
            new_name='Customer_address',
        ),
        migrations.RenameField(
            model_name='exhibition',
            old_name='Loc',
            new_name='E_Location',
        ),
        migrations.RenameField(
            model_name='exhibition',
            old_name='G_ID',
            new_name='Gallery_ID',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Ord_desc',
            new_name='Order_desc',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Ord_no',
            new_name='Order_no',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Ord_type',
            new_name='Order_type',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='P_bill',
            new_name='Payment_bill',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='P_date',
            new_name='Payment_date',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='P_desc',
            new_name='Payment_desc',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='P_type',
            new_name='Payment_type',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='C_phone',
        ),
        migrations.AddField(
            model_name='customer',
            name='Customer_phone',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='Address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='Phone',
            field=models.CharField(max_length=100),
        ),
    ]
