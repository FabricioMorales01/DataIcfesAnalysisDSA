import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IcfesDashboardComponent } from './icfes-dashboard.component';

describe('IcfesDashboardComponent', () => {
  let component: IcfesDashboardComponent;
  let fixture: ComponentFixture<IcfesDashboardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IcfesDashboardComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(IcfesDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
