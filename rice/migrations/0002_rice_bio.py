# Generated by Django 3.0.5 on 2021-01-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rice_Bio',
            fields=[
                ('ID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Rice_Varieties', models.CharField(max_length=100)),
                ('Tocopherol_Alpha_M', models.CharField(max_length=50)),
                ('Tocopherol_Alpha_U', models.CharField(max_length=50)),
                ('Tocopherol_Alpha', models.CharField(max_length=50)),
                ('Tocopherol_Beta_M', models.CharField(max_length=50)),
                ('Tocopherol_Beta_U', models.CharField(max_length=50)),
                ('Tocopherol_Beta', models.CharField(max_length=50)),
                ('Tocopherol_Gamma_M', models.CharField(max_length=50)),
                ('Gamma_tocopherol_M', models.CharField(max_length=50)),
                ('Tocopherol_Gamma_U', models.CharField(max_length=50)),
                ('Tocopherol_Gamma', models.CharField(max_length=50)),
                ('Tocopherol_Sigma_M', models.CharField(max_length=50)),
                ('Tocopherol_Sigma_U', models.CharField(max_length=50)),
                ('Tocopherol_Delta_M', models.CharField(max_length=50)),
                ('Tocopherol_Delta_U', models.CharField(max_length=50)),
                ('Tocotrienol_Alpha_M', models.CharField(max_length=50)),
                ('Tocotrienol_Alpha_U', models.CharField(max_length=50)),
                ('Tocotrienol_Beta_M', models.CharField(max_length=50)),
                ('Tocotrienol_Beta_U', models.CharField(max_length=50)),
                ('Tocotrienol_Gamma_M_mg', models.CharField(max_length=50)),
                ('Tocotrienol_Gamma_M', models.CharField(max_length=50)),
                ('Tocotrienol_Gamma_U', models.CharField(max_length=50)),
                ('Tocotrienol_Sigma_M', models.CharField(max_length=50)),
                ('Tocotrienol_Sigma_U', models.CharField(max_length=50)),
                ('Tocotrienol_Delta_M', models.CharField(max_length=50)),
                ('Tocotrienol_Delta_U', models.CharField(max_length=50)),
                ('Prolamine', models.CharField(max_length=50)),
                ('Albumin', models.CharField(max_length=50)),
                ('Globulin', models.CharField(max_length=50)),
                ('Glutenin', models.CharField(max_length=50)),
                ('Omega_3', models.CharField(max_length=50)),
                ('Omega_6', models.CharField(max_length=50)),
                ('Omega_9', models.CharField(max_length=50)),
                ('Tryptophan_M', models.CharField(max_length=50)),
                ('Tryptophan_U', models.CharField(max_length=50)),
                ('Threonine_M', models.CharField(max_length=50)),
                ('Threonine_U', models.CharField(max_length=50)),
                ('Isoleucine_M', models.CharField(max_length=50)),
                ('Isoleucine_U', models.CharField(max_length=50)),
                ('Leucine_M', models.CharField(max_length=50)),
                ('Leucine_U', models.CharField(max_length=50)),
                ('Lysine_M', models.CharField(max_length=50)),
                ('Lysine_U', models.CharField(max_length=50)),
                ('Methionine_M', models.CharField(max_length=50)),
                ('Methionine_U', models.CharField(max_length=50)),
                ('Cystine_M', models.CharField(max_length=50)),
                ('Cystine_U', models.CharField(max_length=50)),
                ('Phenylalanine_M', models.CharField(max_length=50)),
                ('Phenylalanine_U', models.CharField(max_length=50)),
                ('Tyrosine_M', models.CharField(max_length=50)),
                ('Tyrosine_U', models.CharField(max_length=50)),
                ('Valine_M', models.CharField(max_length=50)),
                ('Valine_U', models.CharField(max_length=50)),
                ('Arginnine_M', models.CharField(max_length=50)),
                ('Arginnine_U', models.CharField(max_length=50)),
                ('Histidine_M', models.CharField(max_length=50)),
                ('Histidine_U', models.CharField(max_length=50)),
                ('Alanine_M', models.CharField(max_length=50)),
                ('Alanine_U', models.CharField(max_length=50)),
                ('Aspartic_acid_M', models.CharField(max_length=50)),
                ('Aspartic_acid_U', models.CharField(max_length=50)),
                ('Glutamic_acid_M', models.CharField(max_length=50)),
                ('Glutamic_acid_U', models.CharField(max_length=50)),
                ('Glycine_M', models.CharField(max_length=50)),
                ('Glycine_U', models.CharField(max_length=50)),
                ('Proline_M', models.CharField(max_length=50)),
                ('Proline_U', models.CharField(max_length=50)),
                ('Serine_M', models.CharField(max_length=50)),
                ('Serine_U', models.CharField(max_length=50)),
                ('Cerine_M', models.CharField(max_length=50)),
                ('Cerine_U', models.CharField(max_length=50)),
                ('Ethyl_alcohol', models.CharField(max_length=50)),
                ('Caffeine', models.CharField(max_length=50)),
                ('Theobromine', models.CharField(max_length=50)),
                ('Beta_carotene', models.CharField(max_length=50)),
                ('Alpha_carotene', models.CharField(max_length=50)),
                ('Beta_cryptoxanthin', models.CharField(max_length=50)),
                ('Lycopene', models.CharField(max_length=50)),
                ('Lutein_Zeaxanthin', models.CharField(max_length=50)),
                ('Biotin_U', models.CharField(max_length=50)),
                ('Gamma_Oryzanol_M', models.CharField(max_length=50)),
                ('Gamma_Oryzanol_U', models.CharField(max_length=50)),
                ('Phenolic_compounds', models.CharField(max_length=50)),
                ('Total_Antioxidant_M', models.CharField(max_length=50)),
                ('Total_Antioxidant_U', models.CharField(max_length=50)),
                ('Total_Antioxidant_M_Tr', models.CharField(max_length=50)),
                ('Total_Antioxidant', models.CharField(max_length=50)),
                ('Antioxidant_compounds', models.CharField(max_length=50)),
                ('Gallic_acid_M', models.CharField(max_length=50)),
                ('Gallic_acid', models.CharField(max_length=50)),
                ('Eriodictyol_M', models.CharField(max_length=50)),
                ('Eriodictyol', models.CharField(max_length=50)),
                ('Anthocyanin', models.CharField(max_length=50)),
                ('Apigenin_M', models.CharField(max_length=50)),
                ('Apigenin', models.CharField(max_length=50)),
                ('Isoquercetin_M', models.CharField(max_length=50)),
                ('Isoquercetin', models.CharField(max_length=50)),
                ('Hydroquinin_M', models.CharField(max_length=50)),
                ('Hydroquinin', models.CharField(max_length=50)),
                ('Quercetin_M', models.CharField(max_length=50)),
                ('Quercetin', models.CharField(max_length=50)),
                ('Kaempferol_M', models.CharField(max_length=50)),
                ('Kaempferol', models.CharField(max_length=50)),
                ('Rutin_M', models.CharField(max_length=50)),
                ('Rutin', models.CharField(max_length=50)),
                ('Catechin_M', models.CharField(max_length=50)),
                ('Catechin', models.CharField(max_length=50)),
                ('Tannic_acid_M', models.CharField(max_length=50)),
                ('Tannic_acid', models.CharField(max_length=50)),
                ('Flavonoid', models.CharField(max_length=50)),
                ('GABA_gamma_Aminobutyric_acid', models.CharField(max_length=50)),
                ('Total_Tocopherol', models.CharField(max_length=50)),
                ('Genistein', models.CharField(max_length=50)),
                ('Daidzien', models.CharField(max_length=50)),
                ('Genistin', models.CharField(max_length=50)),
                ('Daidzin', models.CharField(max_length=50)),
                ('Quercitin3BDGlucoside', models.CharField(max_length=50)),
                ('Peonidin3Oglucoside', models.CharField(max_length=50)),
                ('Oenin', models.CharField(max_length=50)),
            ],
        ),
    ]
