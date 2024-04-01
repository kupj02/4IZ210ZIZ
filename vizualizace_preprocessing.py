import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from collections import Counter

from preprocessing import train_df, test_df


# Funkce pro vizualizaci dat s překrytím trénovacích a testovacích sad
def visualize_data(train_data, test_data, axs):
    # Definice barev pro trénovací a testovací množiny
    train_color = 'blue'
    test_color = 'orange'

    # Histogramy a grafy rozptylu s váhami
    for ax, feature in zip(axs[:4], ['stroke', 'smoking_status', 'age', 'bmi']):
        # Trenovaci set
        ax.hist(train_data[feature], bins=30, color=train_color, alpha=0.5, label='Train')
        # Testovaci set
        ax.hist(test_data[feature], bins=30, color=test_color, alpha=0.5, label='Test')
        ax.set_title(f'Histogram of {feature.capitalize()}')

    # Graf rozptylu Age vs Stroke
    c_age_train = Counter(zip(train_data['age'], train_data['stroke']))
    axs[4].scatter(train_data['age'], train_data['stroke'],
                   s=[5 * c_age_train[(x, y)] for x, y in zip(train_data['age'], train_data['stroke'])],
                   color=train_color, alpha=0.5, label='Train')

    c_age_test = Counter(zip(test_data['age'], test_data['stroke']))
    axs[4].scatter(test_data['age'], test_data['stroke'],
                   s=[5 * c_age_test[(x, y)] for x, y in zip(test_data['age'], test_data['stroke'])],
                   color=test_color, alpha=0.5, label='Test')
    axs[4].set_title('Scatter Plot of Age vs Stroke')

    # Graf rozptylu BMI vs Stroke
    c_bmi_train = Counter(zip(train_data['bmi'], train_data['stroke']))
    axs[5].scatter(train_data['bmi'], train_data['stroke'],
                   s=[5 * c_bmi_train[(x, y)] for x, y in zip(train_data['bmi'], train_data['stroke'])],
                   color=train_color, alpha=0.5, label='Train')

    c_bmi_test = Counter(zip(test_data['bmi'], test_data['stroke']))
    axs[5].scatter(test_data['bmi'], test_data['stroke'],
                   s=[5 * c_bmi_test[(x, y)] for x, y in zip(test_data['bmi'], test_data['stroke'])],
                   color=test_color, alpha=0.5, label='Test')
    axs[5].set_title('Scatter Plot of BMI vs Stroke')

    # Pridej legendu
    for ax in axs[:6]:
        ax.legend()


# Vytvoreni obrazku a os pro vizualizace
fig, axs = plt.subplots(2, 3, figsize=(20, 10))
visualize_data(train_df, test_df, axs.flatten())

# Uprava rozvrzeni tak, aby se neprekryvalo a uvolnilo se misto pro nadpis
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# Nastaveni nadpisu s mezerou nad hornimi osami
fig.subplots_adjust(top=0.88)
plt.suptitle('Distributions of Train vs Test Sets', fontsize=16, y=0.98)
plt.show()
