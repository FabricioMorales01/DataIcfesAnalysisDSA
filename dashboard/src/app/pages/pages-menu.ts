import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'Dashboard icfes',
    icon: 'pie-chart-outline',
    link: '/pages/dashboard-icfes',
    home: true,
  },
  {
    title: 'Dashboard demo 1',
    icon: 'shopping-cart-outline',
    link: '/pages/dashboard',
    home: true,
  },
  {
    title: 'Dashboard demo2',
    icon: 'home-outline',
    link: '/pages/iot-dashboard',
  },
  {
    title: 'Herramientas',
    group: true,
  },
  {
    title: 'Predecir',
    icon: 'browser-outline',
    link: '/pages/forms/layouts',
  },
  {
    title: 'Resultados en el mundo',
    icon: 'map-outline',
    link: '/pages/maps/bubble',
  },
];
