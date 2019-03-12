/**
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for
 * license information.
 */

package com.microsoft.rest.v3.util;

import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Utility type exposing methods to deal with {@link Type}.
 */
public final class TypeUtil {
    /**
     * Find all super classes including provided class.
     *
     * @param clazz the raw class to find super types for
     * @return the list of super classes
     */
    public static List<Class<?>> getAllClasses(Class<?> clazz) {
        List<Class<?>> types = new ArrayList<>();
        while (clazz != null) {
            types.add(clazz);
            clazz = clazz.getSuperclass();
        }
        return types;
    }

    /**
     * Get the generic arguments for a type.
     *
     * @param type the type to get arguments
     * @return the generic arguments, empty if type is not parametrized
     */
    public static Type[] getTypeArguments(Type type) {
        if (!(type instanceof ParameterizedType)) {
            return new Type[0];
        }
        return ((ParameterizedType) type).getActualTypeArguments();
    }

    /**
     * Get the generic argument, or the first if the type has more than one.
     *
     * @param type the type to get arguments
     * @return the generic argument, null if type is not parametrized
     */
    public static Type getTypeArgument(Type type) {
        if (!(type instanceof ParameterizedType)) {
            return null;
        }
        return ((ParameterizedType) type).getActualTypeArguments()[0];
    }

    /**
     * Get the raw class for a given type.
     *
     * @param type the input type
     * @return the raw class
     */
    public static Class<?> getRawClass(Type type) {
        if (type instanceof ParameterizedType) {
            return (Class<?>) ((ParameterizedType) type).getRawType();
        } else {
            return (Class<?>) type;
        }
    }

    /**
     * Get the super type for a given type.
     *
     * @param type the input type
     * @return the direct super type
     */
    public static Type getSuperType(Type type) {
        if (type instanceof ParameterizedType) {
            ParameterizedType parameterizedType = (ParameterizedType) type;
            Type genericSuperClass = ((Class<?>) parameterizedType.getRawType()).getGenericSuperclass();
            if (genericSuperClass instanceof ParameterizedType) {
                /*
                 * Find erased generic types for the super class and replace
                 * with actual type arguments from the parametrized type
                 */
                Type[] superTypeArguments = getTypeArguments(genericSuperClass);
                List<Type> typeParameters = Arrays.asList(((Class<?>) parameterizedType.getRawType()).getTypeParameters());
                int j = 0;
                for (int i = 0; i != superTypeArguments.length; i++) {
                    if (typeParameters.contains(superTypeArguments[i])) {
                        superTypeArguments[i] = parameterizedType.getActualTypeArguments()[j++];
                    }
                }
                return new ParameterizedType() {
                    @Override
                    public Type[] getActualTypeArguments() {
                        return superTypeArguments;
                    }

                    @Override
                    public Type getRawType() {
                        return ((ParameterizedType) genericSuperClass).getRawType();
                    }

                    @Override
                    public Type getOwnerType() {
                        return null;
                    }
                };
            } else {
                return genericSuperClass;
            }
        } else {
            return ((Class<?>) type).getGenericSuperclass();
        }
    }

    /**
     * Get the super type for a type in its super type chain, which has
     * a raw class that matches the specified class.
     *
     * @param subType the sub type to find super type for
     * @param rawSuperType the raw class for the super type
     * @return the super type that matches the requirement
     */
    public static Type getSuperType(Type subType, Class<?> rawSuperType) {
        while (subType != null && getRawClass(subType) != rawSuperType) {
            subType = getSuperType(subType);
        }
        return subType;
    }

    /**
     * Determines if a type is the same or a subtype for another type.
     * 
     * @param subType the supposed sub type
     * @param superType the supposed super type
     * @return true if the first type is the same or a subtype for the second type
     */
    public static boolean isTypeOrSubTypeOf(Type subType, Type superType) {
        Class<?> sub = getRawClass(subType);
        Class<?> sup = getRawClass(superType);

        return sup.isAssignableFrom(sub);
    }

    /**
     * Create a parametrized type from a raw class and its type arguments.
     *
     * @param rawClass the raw class to construct the parametrized type
     * @param genericTypes the generic arguments
     * @return the parametrized type
     */
    public static ParameterizedType createParameterizedType(Class<?> rawClass, Type... genericTypes) {
        return new ParameterizedType() {
            @Override
            public Type[] getActualTypeArguments() {
                return genericTypes;
            }

            @Override
            public Type getRawType() {
                return rawClass;
            }

            @Override
            public Type getOwnerType() {
                return null;
            }
        };
    }

    /**
     * Returns whether the rest response expects to have any body (by checking if the body parameter type is set to Void,
     * in which case no body is expected).
     *
     * @param restResponseReturnType The RestResponse subtype containing the type arguments we are inspecting.
     * @return True if a body is expected, false if a Void body is expected.
     */
    public static boolean restResponseTypeExpectsBody(ParameterizedType restResponseReturnType) {
        return getRestResponseBodyType(restResponseReturnType) != Void.class;
    }

    /**
     * Returns the body type expected in the rest response.
     *
     * @param restResponseReturnType The RestResponse subtype containing the type arguments we are inspecting.
     * @return The type of the body.
     */
    public static Type getRestResponseBodyType(Type restResponseReturnType) {
        // if this type has type arguments, then we look at the last one to determine if it expects a body
        final Type[] restResponseTypeArguments = TypeUtil.getTypeArguments(restResponseReturnType);
        if (restResponseTypeArguments != null && restResponseTypeArguments.length > 0) {
            return restResponseTypeArguments[restResponseTypeArguments.length - 1];
        } else {
            // no generic type on this RestResponse sub-type, so we go up to parent
            return getRestResponseBodyType(TypeUtil.getSuperType(restResponseReturnType));
        }
    }

    // Private Ctr
    private TypeUtil() {
    }
}
