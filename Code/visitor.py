from Code.plot_circle import *


class PrettyPrinter:
    def __init__(self):
        self.indent = 0
        return

    def visite_program(self, program):

        out = 'figure ' + program.name.accept(self) + ' {' + \
              '\n'
        self.indent += 1
        out += program.declarations.accept(self) + \
                 '\n' + \
              program.to_draw.accept(self) + '}\n______________________\n'
        self.indent -= 1  # En réalité avec ce langage, il n'y a pas de problème d'indentation

        return out


    def visite_body_draw(self, body_draw):
        out = ''
        for d in body_draw.to_draw:
            out += self.indent * '\t' + d.accept(self) + '\n'
        return out

    def visite_draw(self, draw):
        out = 'draw ' + draw.expr.accept(self)
        return out

    def visite_body_declaration(self, body_declaration):
        out = ''
        for d in body_declaration.declarations:
            out += self.indent * '\t' + d.accept(self) + '\n'
        return out

    def visite_declaration(self, declaration):
        out = declaration.ident.accept(self) + ' = ' + declaration.expr.accept(self)
        return out

    def visite_expression(self, expression):
        return expression.value.accept(self)

    def visite_point(self, point):
        out = '(' + point.x.accept(self) + ', ' + point.y.accept(self) + ')'
        return out

    def visite_circle(self, circle):
        out = '(' + circle.radius.accept(self) + ', ' + circle.center.accept(self) + ')'
        return out

    def visite_droite(self, droite):
        out = '(' + droite.point1.accept(self) + ', ' + droite.point2.accept(self) + ')'
        return out

    def visite_segment(self, segment):
        out = '[\n'
        self.indent += 1
        for i in range(len(segment.point)-1):
            out += self.indent * '\t' + segment.point[i].accept(self) + ',\n'
        out += self.indent * '\t' + segment.point[-1].accept(self) + '\n' + self.indent * '\t' +']' + '\n'
        self.indent -= 1
        return out

    def visite_name(self, name):
        return name.name.accept(self)

    def visite_distance(self, distance):
        return distance.value.accept(self)


    @staticmethod
    def visite_lexem(lexem):
        return lexem.value


class DrawVisitor:
    def __init__(self, compilator):
        self.compilator = compilator
        return

    def visite_point(self, point):
        self.compilator.ax.plot(point.x.accept(self), point.y.accept(self), 'ro')

    def visite_circle(self, circle):
        X, Y = create_circle((circle.center.x.accept(self), circle.center.y.accept(self)),
                             circle.radius.accept(self))

        self.compilator.ax.plot(X, Y, 'r')
        return

    def visite_droite(self, droite):
        self.compilator.ax.plot([droite.point1.x.accept(self), droite.point2.x.accept(self)],
                           [droite.point1.y.accept(self), droite.point2.y.accept(self)], 'r')

        return

    def visite_segment(self, segment):
        for i in range(len(segment.point) - 1):
            self.compilator.ax.plot([segment.point[i].x.accept(self), segment.point[i + 1].x.accept(self)],
                                 [segment.point[i].y.accept(self), segment.point[i + 1].y.accept(self)], 'r')
        return

    def visite_distance(self, distance):
        return distance.value.accept(self)

    def visite_lexem(self, lexem):
        if lexem.kind == 'ident':
            # Cet appel récursif permet de remonter à la valeur numérique de l'identifiant pour le dessiner
            return self.compilator.parseur.value_ident[lexem.value].accept(self)
        else:
            return float(lexem.value)