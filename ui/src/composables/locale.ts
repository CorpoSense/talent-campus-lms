
const supportedLanguages = ['en', 'ar', 'fr'];

export function getSupportedLanguages() {
    return supportedLanguages;
}

export function usePreferredLanguage() {
    const defaultLocale = supportedLanguages[0];
    let userLanguage = defaultLocale;
    if (typeof window !== 'undefined'){
        userLanguage = (navigator.languages[0] || navigator.language || (navigator as any).browserLanguage || (navigator as any).systemLanguage || (navigator as any).userLanguage || import.meta.env.VITE_LOCALE)
    } else {
        userLanguage = import.meta.env.VITE_LOCALE || defaultLocale;
    }
    return userLanguage.split('-')[0]
}
