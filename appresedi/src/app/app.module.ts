import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';
import { AngularFireModule } from '@angular/fire';
import { AngularFireDatabaseModule } from '@angular/fire/database';


import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [AppComponent],
  entryComponents: [],
  imports: [
    BrowserModule,
    IonicModule.forRoot(),
    AppRoutingModule, AngularFireDatabaseModule, AngularFireModule.initializeApp({
      apiKey: "AIzaSyA41eCj_17Er-L780I2iKjNBMcHg7T2Oy8",
    authDomain: "reservaif.firebaseapp.com",
    databaseURL: "https://reservaif.firebaseio.com",
    projectId: "reservaif",
    storageBucket: "reservaif.appspot.com",
    messagingSenderId: "126684095995",
    appId: "1:126684095995:web:ffe4da0bc6a706e84d575e"
    })
  ],
  providers: [
    StatusBar,
    SplashScreen,
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
