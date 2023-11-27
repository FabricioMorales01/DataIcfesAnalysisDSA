import { NgModule } from '@angular/core';
import {
  NbFormFieldModule, NbButtonModule, NbCardModule, NbCheckboxModule, NbDatepickerModule, NbIconModule, NbInputModule, NbMenuModule,
   NbRadioModule,
  NbSelectModule, 
  NbWindowModule,
  NbAutocompleteModule} from '@nebular/theme';

import { ThemeModule } from '../@theme/theme.module';
import { PagesComponent } from './pages.component';
import { PagesRoutingModule } from './pages-routing.module';
import { IcfesDashboardComponent } from './icfes-dashboard/icfes-dashboard.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  imports: [
    PagesRoutingModule,
    ThemeModule,
    NbMenuModule,
    NbButtonModule,
    NbInputModule,
    NbCardModule,
    NbCheckboxModule,
    NbRadioModule,
    NbDatepickerModule,
    NbSelectModule,
    NbIconModule,
    NbFormFieldModule,
    NbAutocompleteModule,
    FormsModule,
    NbWindowModule.forChild(),
  ],
  declarations: [
    PagesComponent,
    IcfesDashboardComponent,
  ],
})
export class PagesModule {
}
