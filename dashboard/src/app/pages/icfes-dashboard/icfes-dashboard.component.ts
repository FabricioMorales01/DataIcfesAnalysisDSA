import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';
import { NbWindowService } from '@nebular/theme';
import { Observable, of } from 'rxjs';
import { data } from '../../@core/data/data'
import { PredictService } from '../../servers/predict.service';

@Component({
  selector: 'ngx-icfes-dashboard',
  templateUrl: './icfes-dashboard.component.html',
  styleUrls: ['./icfes-dashboard.component.scss']
})
export class IcfesDashboardComponent implements OnInit {
  filteredInstitutos$: Observable<any[]>;
  isFrameLoaded = false;
  data = {
    ESTU_GRADO: null,
    COLE_COD_ICFES: null,
    COLE_COD_MCPIO: null,
    COLE_COD_DPTO: null,
    EXA_C_RTAS_CORR_CN: 0,
    EXA_C_RTAS_CORR_CC: 0,
    EXA_C_RTAS_CORR_MT: 0,
    ESTU_GENERO_F: null,
    COLE_NATURALEZA_O: null,
    COLE_JORNADA_COMPLETA: false,
    COLE_JORNADA_MAÑANA: false,
    COLE_JORNADA_TARDE: false,
    EXA_MODALIDAD_OFF: false,
    EXA_MODALIDAD_ON: false,
    EXA_MODALIDAD_PA: false
  };
  grades = [];
  institutos = data;
  isPredicted = false;
  categorias = [
    'Nivel bajo de lectura',
    'Nivel medio de lectura',
    'Nivel alto de lectura',
  ];
  categoria = '';


  @ViewChild('tplWindow', { read: TemplateRef, static: true }) windowTemplate: TemplateRef<HTMLElement>;

  get datas(): string {
    return JSON.stringify(this.data, null, 2);
  }

  constructor(private windowService: NbWindowService, private predictService: PredictService) {}

  ngOnInit(): void {
    this.data = {
      ESTU_GRADO: null,
      COLE_COD_ICFES: null,
      COLE_COD_MCPIO: null,
      COLE_COD_DPTO: null,
      EXA_C_RTAS_CORR_CN: 0,
      EXA_C_RTAS_CORR_CC: 0,
      EXA_C_RTAS_CORR_MT: 0,
      ESTU_GENERO_F: null,
      COLE_NATURALEZA_O: null,
      COLE_JORNADA_COMPLETA: false,
      COLE_JORNADA_MAÑANA: false,
      COLE_JORNADA_TARDE: false,
      EXA_MODALIDAD_OFF: false,
      EXA_MODALIDAD_ON: false,
      EXA_MODALIDAD_PA: false
    };

    // Grade
    this.grades = [];
    for (let i=3; i<= 11; i++) {
      this.grades.push(i);
    }

    // Institutos
    this.filteredInstitutos$ = of(this.institutos);
  }

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

  changeModalidad(modalidad): void {
    this.data.EXA_MODALIDAD_OFF = false;
    this.data.EXA_MODALIDAD_ON = false;
    this.data.EXA_MODALIDAD_PA = false;

    switch(modalidad) {
      case 1:
        this.data.EXA_MODALIDAD_ON = true;  
      break;
      case 2:
        this.data.EXA_MODALIDAD_OFF = true;
      break;
      case 3:
        this.data.EXA_MODALIDAD_PA = true;
      break;
    }
  }

  changeJornada(modalidad): void {
    this.data.COLE_JORNADA_COMPLETA = false;
    this.data.COLE_JORNADA_MAÑANA = false;
    this.data.COLE_JORNADA_TARDE = false;

    switch(modalidad) {
      case 1:
        this.data.COLE_JORNADA_MAÑANA = true;  
      break;
      case 2:
        this.data.COLE_JORNADA_TARDE = true;
      break;
      case 3:
        this.data.COLE_JORNADA_COMPLETA = true;
      break;
    }
  }

  selectInsituto(name): void {
    const instituto = this.institutos.find(d => d.COLE_NOM_ESTABLECIMIENTO === name);

    this.data.COLE_COD_ICFES = instituto.COLE_COD_ICFES;
    this.data.COLE_COD_MCPIO = instituto.COLE_COD_MCPIO;
    this.data.COLE_COD_DPTO = instituto.COLE_COD_DPTO;
    this.data.COLE_NATURALEZA_O = instituto.COLE_NATURALEZA_O;
  }

  changeInstituto(insituto): void {
    this.filteredInstitutos$ = of(this.filter(insituto));
  }

  enviar(): void {
    this.isPredicted = false;
    this.predictService.predict(this.data).subscribe((res: any) => {
      const pred = res.predictions[0] || 0;
      this.categoria = this.categoria[pred];
      this.isPredicted = true;
    },() => {
      alert('Un error ocurrio en la predicción');
    });
  }

  private filter(value: string): any[] {
    const filterValue = value.toLowerCase();
    return this.institutos.filter(optionValue => optionValue.COLE_NOM_ESTABLECIMIENTO.toLowerCase().includes(filterValue));
  }
}
