import { Component, TemplateRef, ViewChild } from '@angular/core';
import { NbWindowService } from '@nebular/theme';

@Component({
  selector: 'ngx-icfes-dashboard',
  templateUrl: './icfes-dashboard.component.html',
  styleUrls: ['./icfes-dashboard.component.scss']
})
export class IcfesDashboardComponent {
  isFrameLoaded = false;

  @ViewChild('tplWindow', { read: TemplateRef, static: true }) windowTemplate: TemplateRef<HTMLElement>;

  constructor(private windowService: NbWindowService) {}

  showButtons(): void {
    this.isFrameLoaded = true;
  }

  showPredict(): void {
    this.windowService.open(
      this.windowTemplate,
      {
        title: 'Predecir respuestas correctas de Lectura',
        closeOnEsc: false,
      },
    );
  }
}
