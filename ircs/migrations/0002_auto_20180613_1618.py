# Generated by Django 2.0.4 on 2018-06-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ircs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABO_and_Rh_on_Patient_S6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell_forward_typing_method_used', models.TextField(blank=True)),
                ('Anti_A', models.IntegerField(default=0)),
                ('Anti_B', models.IntegerField(default=0)),
                ('Anti_ABpositive', models.IntegerField(default=0)),
                ('Anti_D', models.IntegerField(default=0)),
                ('serum_reverse_group_method_used', models.TextField(blank=True)),
                ('Acells', models.IntegerField(default=0)),
                ('Bcells', models.IntegerField(default=0)),
                ('Ocells', models.IntegerField(default=0)),
                ('Result', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ABO_and_Rh_on_Patient',
        ),
        migrations.DeleteModel(
            name='Sample_Identification_Scoring',
        ),
        migrations.DeleteModel(
            name='Sample_Identification_Scoring_on_Donors',
        ),
        migrations.DeleteModel(
            name='Sample_Identification_Scoring_on_Patient',
        ),
        migrations.RenameField(
            model_name='abo_and_rh_on_donors',
            old_name='AchievableScore',
            new_name='Acells_S7',
        ),
        migrations.RenameField(
            model_name='abo_and_rh_on_donors',
            old_name='YourScore',
            new_name='Acells_S8',
        ),
        migrations.RenameField(
            model_name='compatibility_testing',
            old_name='SampleNo7_and_10',
            new_name='Would_transfer7to10',
        ),
        migrations.RenameField(
            model_name='compatibility_testing',
            old_name='SampleNo8_and_11',
            new_name='Would_transfer8to11',
        ),
        migrations.RenameField(
            model_name='compatibility_testing',
            old_name='SampleNo9_and_12',
            new_name='Would_transfer9to12',
        ),
        migrations.RemoveField(
            model_name='abo_and_rh_on_donors',
            name='SampleNo7',
        ),
        migrations.RemoveField(
            model_name='abo_and_rh_on_donors',
            name='SampleNo8',
        ),
        migrations.RemoveField(
            model_name='abo_and_rh_on_donors',
            name='SampleNo9',
        ),
        migrations.RemoveField(
            model_name='anti_hcv',
            name='AchievableScore',
        ),
        migrations.RemoveField(
            model_name='anti_hcv',
            name='SampleNo1',
        ),
        migrations.RemoveField(
            model_name='anti_hcv',
            name='SampleNo2',
        ),
        migrations.RemoveField(
            model_name='anti_hcv',
            name='SampleNo3',
        ),
        migrations.RemoveField(
            model_name='anti_hcv',
            name='SampleNo4',
        ),
        migrations.RemoveField(
            model_name='anti_hcv',
            name='SampleNo5',
        ),
        migrations.RemoveField(
            model_name='anti_hcv',
            name='YourScore',
        ),
        migrations.RemoveField(
            model_name='anti_hiv',
            name='AchievableScore',
        ),
        migrations.RemoveField(
            model_name='anti_hiv',
            name='SampleNo1',
        ),
        migrations.RemoveField(
            model_name='anti_hiv',
            name='SampleNo2',
        ),
        migrations.RemoveField(
            model_name='anti_hiv',
            name='SampleNo3',
        ),
        migrations.RemoveField(
            model_name='anti_hiv',
            name='SampleNo4',
        ),
        migrations.RemoveField(
            model_name='anti_hiv',
            name='SampleNo5',
        ),
        migrations.RemoveField(
            model_name='anti_hiv',
            name='YourScore',
        ),
        migrations.RemoveField(
            model_name='compatibility_testing',
            name='AchievableScore',
        ),
        migrations.RemoveField(
            model_name='compatibility_testing',
            name='YourScore',
        ),
        migrations.RemoveField(
            model_name='direct_anti_globin_test',
            name='AchievableScore',
        ),
        migrations.RemoveField(
            model_name='direct_anti_globin_test',
            name='YourScore',
        ),
        migrations.RemoveField(
            model_name='haemoglobin',
            name='AchievableScore',
        ),
        migrations.RemoveField(
            model_name='haemoglobin',
            name='SampleNo6_Mean_Value',
        ),
        migrations.RemoveField(
            model_name='haemoglobin',
            name='SampleNo6_Sat_or_Not_Sat',
        ),
        migrations.RemoveField(
            model_name='haemoglobin',
            name='SampleNo6_Your_Result',
        ),
        migrations.RemoveField(
            model_name='haemoglobin',
            name='SampleNo6_Your_SDI_Value',
        ),
        migrations.RemoveField(
            model_name='haemoglobin',
            name='SampleNo7_Mean_Value',
        ),
        migrations.RemoveField(
            model_name='haemoglobin',
            name='SampleNo7_Sat_or_Not_Sat',
        ),
        migrations.RemoveField(
            model_name='haemoglobin',
            name='SampleNo7_Your_Result',
        ),
        migrations.RemoveField(
            model_name='haemoglobin',
            name='SampleNo7_Your_SDI_Value',
        ),
        migrations.RemoveField(
            model_name='haemoglobin',
            name='YourScore',
        ),
        migrations.RemoveField(
            model_name='hbsag',
            name='AchievableScore',
        ),
        migrations.RemoveField(
            model_name='hbsag',
            name='SampleNo1',
        ),
        migrations.RemoveField(
            model_name='hbsag',
            name='SampleNo2',
        ),
        migrations.RemoveField(
            model_name='hbsag',
            name='SampleNo3',
        ),
        migrations.RemoveField(
            model_name='hbsag',
            name='SampleNo4',
        ),
        migrations.RemoveField(
            model_name='hbsag',
            name='SampleNo5',
        ),
        migrations.RemoveField(
            model_name='hbsag',
            name='YourScore',
        ),
        migrations.RemoveField(
            model_name='malaria_parasite',
            name='AchievableScore',
        ),
        migrations.RemoveField(
            model_name='malaria_parasite',
            name='YourScore',
        ),
        migrations.RemoveField(
            model_name='syphilis',
            name='AchievableScore',
        ),
        migrations.RemoveField(
            model_name='syphilis',
            name='SampleNo1',
        ),
        migrations.RemoveField(
            model_name='syphilis',
            name='SampleNo2',
        ),
        migrations.RemoveField(
            model_name='syphilis',
            name='SampleNo3',
        ),
        migrations.RemoveField(
            model_name='syphilis',
            name='SampleNo4',
        ),
        migrations.RemoveField(
            model_name='syphilis',
            name='SampleNo5',
        ),
        migrations.RemoveField(
            model_name='syphilis',
            name='YourScore',
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Acells_S9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_ABpositive_S7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_ABpositive_S8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_ABpositive_S9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_A_S7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_A_S8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_A_S9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_B_S7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_B_S8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_B_S9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_D_S7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_D_S8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Anti_D_S9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Bcells_S7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Bcells_S8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Bcells_S9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Ocells_S7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Ocells_S8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Ocells_S9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Result_S7',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Result_S8',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='Result_S9',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='cell_forward_typing_method_used',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='abo_and_rh_on_donors',
            name='serum_reverse_group_method_used',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='CutOffValue',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='Methodology',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='SampleNo1_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='SampleNo1_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='SampleNo2_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='SampleNo2_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='SampleNo3_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='SampleNo3_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='SampleNo4_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='SampleNo4_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='SampleNo5_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hcv',
            name='SampleNo5_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='CutOffValue',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='Methodology',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='SampleNo1_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='SampleNo1_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='SampleNo2_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='SampleNo2_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='SampleNo3_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='SampleNo3_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='SampleNo4_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='SampleNo4_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='SampleNo5_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='anti_hiv',
            name='SampleNo5_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='MethodUsed',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo7D_and_10R_Additive_37degC',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo7D_and_10R_Additive_Room_temp',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo7D_and_10R_IAHG',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo7D_and_10R_Saline_Room_temp',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo8D_and_11R_Additive_37degC',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo8D_and_11R_Additive_Room_temp',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo8D_and_11R_IAHG',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo8D_and_11R_Saline_Room_temp',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo9D_and_12R_Additive_37degC',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo9D_and_12R_Additive_Room_temp',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo9D_and_12R_IAHG',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='SampleNo9D_and_12R_Saline_Room_temp',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='Specifiy_additive',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='compatibility_testing',
            name='Specifiy_other_method',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='haemoglobin',
            name='Methodology',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='haemoglobin',
            name='SampleNo6',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='haemoglobin',
            name='SampleNo7',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='CutOffValue',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='Methodology',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='SampleNo1_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='SampleNo1_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='SampleNo2_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='SampleNo2_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='SampleNo3_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='SampleNo3_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='SampleNo4_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='SampleNo4_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='SampleNo5_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hbsag',
            name='SampleNo5_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='malaria_parasite',
            name='Methodology',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='CutOffValue',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='Methodology',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='SampleNo1_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='SampleNo1_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='SampleNo2_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='SampleNo2_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='SampleNo3_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='SampleNo3_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='SampleNo4_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='SampleNo4_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='SampleNo5_OD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='syphilis',
            name='SampleNo5_Result',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='malaria_parasite',
            name='SampleNo6',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='malaria_parasite',
            name='SampleNo7',
            field=models.TextField(blank=True),
        ),
    ]
