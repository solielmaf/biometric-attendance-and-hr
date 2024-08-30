import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import en from './locales/en.json';
import am from './locales/am.json';

const resources = {
  en: { translation: en },
  am: { translation: am }
};

i18n.use(initReactI18next).init({
  resources,
  lng: 'en', // default language
  fallbackLng: 'en',
  interpolation: { escapeValue: false }
});

export default i18n;
