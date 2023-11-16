/********************************************************************************
** Form generated from reading UI file 'PaintScene.ui'
**
** Created by: Qt User Interface Compiler version 5.15.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PAINTSCENE_H
#define UI_PAINTSCENE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_PaintScene
{
public:

    void setupUi(QWidget *PaintScene)
    {
        if (PaintScene->objectName().isEmpty())
            PaintScene->setObjectName(QString::fromUtf8("PaintScene"));
        PaintScene->resize(400, 300);

        retranslateUi(PaintScene);

        QMetaObject::connectSlotsByName(PaintScene);
    } // setupUi

    void retranslateUi(QWidget *PaintScene)
    {
        PaintScene->setWindowTitle(QCoreApplication::translate("PaintScene", "PaintScene", nullptr));
    } // retranslateUi

};

namespace Ui {
    class PaintScene: public Ui_PaintScene {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PAINTSCENE_H
